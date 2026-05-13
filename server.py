#!/usr/bin/env python3
"""
Food Craft 本地服务器
提供API接口和静态文件服务
"""

import json
import os
import sqlite3
from pathlib import Path
from http.server import HTTPServer, SimpleHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import threading
import webbrowser

BASE_DIR = Path(__file__).parent
DB_PATH = BASE_DIR / "data" / "recipes.db"
RECIPES_DIR = BASE_DIR / "recipes"
FRONTEND_DIR = BASE_DIR / "frontend"

class FoodCraftHandler(SimpleHTTPRequestHandler):
    """自定义HTTP请求处理器"""
    
    def do_GET(self):
        parsed_path = urlparse(self.path)
        
        # API路由
        if parsed_path.path.startswith('/api/'):
            self.handle_api(parsed_path)
        # 静态文件
        elif parsed_path.path == '/' or parsed_path.path == '/index.html':
            self.serve_file(FRONTEND_DIR / 'interactive.html', 'text/html')
        elif parsed_path.path == '/demo':
            self.serve_file(FRONTEND_DIR / 'index.html', 'text/html')
        else:
            # 尝试作为静态文件
            file_path = FRONTEND_DIR / parsed_path.path.lstrip('/')
            if file_path.exists():
                self.serve_static(file_path)
            else:
                self.send_error(404, "File Not Found")
    
    def handle_api(self, parsed_path):
        """处理API请求"""
        path = parsed_path.path
        params = parse_qs(parsed_path.query)
        
        if path == '/api/recipes':
            self.api_recipes(params)
        elif path == '/api/recipes/random':
            self.api_random_recipes(params)
        elif path == '/api/recipes/search':
            self.api_search_recipes(params)
        elif path == '/api/cuisines':
            self.api_cuisines()
        elif path == '/api/scenes':
            self.api_scenes()
        elif path == '/api/stats':
            self.api_stats()
        else:
            self.send_error(404, "API Not Found")
    
    def api_recipes(self, params):
        """获取菜谱列表"""
        cuisine = params.get('cuisine', [None])[0]
        scene = params.get('scene', [None])[0]
        limit = int(params.get('limit', [20])[0])
        
        recipes = self.load_recipes(cuisine, scene, limit)
        
        self.send_json_response({
            'success': True,
            'data': recipes,
            'total': len(recipes)
        })
    
    def api_random_recipes(self, params):
        """获取随机菜谱"""
        count = int(params.get('count', [5])[0])
        cuisine = params.get('cuisine', [None])[0]
        
        recipes = self.load_random_recipes(count, cuisine)
        
        self.send_json_response({
            'success': True,
            'data': recipes
        })
    
    def api_search_recipes(self, params):
        """搜索菜谱"""
        keyword = params.get('keyword', [''])[0]
        limit = int(params.get('limit', [10])[0])
        
        recipes = self.search_recipes(keyword, limit)
        
        self.send_json_response({
            'success': True,
            'data': recipes,
            'keyword': keyword
        })
    
    def api_cuisines(self):
        """获取菜系列表"""
        cuisines = []
        cuisines_dir = RECIPES_DIR
        if cuisines_dir.exists():
            for d in cuisines_dir.iterdir():
                if d.is_dir() and d.name not in ['children', 'elderly', 'weight_loss', 'muscle_gain', 'vegetarian']:
                    count = len(list(d.rglob('*.json')))
                    if count > 0:
                        cuisines.append({
                            'id': d.name,
                            'name': d.name,
                            'count': count
                        })
        
        self.send_json_response({
            'success': True,
            'data': cuisines
        })
    
    def api_scenes(self):
        """获取场景列表"""
        scenes = [
            {'id': 'children', 'name': '儿童餐', 'icon': '👶', 'desc': '3-12岁营养餐'},
            {'id': 'elderly', 'name': '老人餐', 'icon': '👴', 'desc': '65岁以上软烂餐'},
            {'id': 'weight_loss', 'name': '减脂餐', 'icon': '💪', 'desc': '低卡高蛋白'},
            {'id': 'muscle_gain', 'name': '增肌餐', 'icon': '🏋️', 'desc': '高蛋白高热量'},
            {'id': 'vegetarian', 'name': '素食餐', 'icon': '🥬', 'desc': '纯素/蛋奶素'}
        ]
        
        self.send_json_response({
            'success': True,
            'data': scenes
        })
    
    def api_stats(self):
        """获取统计信息"""
        total_recipes = len(list(RECIPES_DIR.rglob('*.json')))
        
        self.send_json_response({
            'success': True,
            'data': {
                'total_recipes': total_recipes,
                'total_ingredients': 1025,
                'total_cuisines': 39,
                'total_scenes': 5
            }
        })
    
    def load_recipes(self, cuisine=None, scene=None, limit=20):
        """加载菜谱"""
        recipes = []
        search_dirs = []
        
        if scene:
            search_dirs.append(RECIPES_DIR / scene / 'special')
        elif cuisine:
            search_dirs.append(RECIPES_DIR / cuisine)
        else:
            search_dirs = [d for d in RECIPES_DIR.iterdir() if d.is_dir()]
        
        for search_dir in search_dirs:
            if not search_dir.exists():
                continue
            for json_file in search_dir.rglob('*.json'):
                if len(recipes) >= limit:
                    break
                try:
                    with open(json_file, 'r', encoding='utf-8') as f:
                        recipe = json.load(f)
                        if 'id' in recipe and 'name' in recipe:
                            recipes.append(recipe)
                except:
                    pass
        
        return recipes
    
    def load_random_recipes(self, count=5, cuisine=None):
        """加载随机菜谱"""
        import random
        all_recipes = self.load_recipes(cuisine=cuisine, limit=1000)
        return random.sample(all_recipes, min(count, len(all_recipes)))
    
    def search_recipes(self, keyword, limit=10):
        """搜索菜谱"""
        results = []
        
        for json_file in RECIPES_DIR.rglob('*.json'):
            if len(results) >= limit:
                break
            try:
                with open(json_file, 'r', encoding='utf-8') as f:
                    recipe = json.load(f)
                    if keyword.lower() in recipe.get('name', '').lower():
                        results.append(recipe)
            except:
                pass
        
        return results
    
    def send_json_response(self, data):
        """发送JSON响应"""
        response = json.dumps(data, ensure_ascii=False, indent=2)
        self.send_response(200)
        self.send_header('Content-Type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(response.encode('utf-8'))
    
    def serve_file(self, file_path, content_type):
        """提供文件服务"""
        if file_path.exists():
            self.send_response(200)
            self.send_header('Content-Type', f'{content_type}; charset=utf-8')
            self.end_headers()
            with open(file_path, 'rb') as f:
                self.wfile.write(f.read())
        else:
            self.send_error(404, "File Not Found")
    
    def serve_static(self, file_path):
        """提供静态文件服务"""
        content_types = {
            '.html': 'text/html',
            '.css': 'text/css',
            '.js': 'application/javascript',
            '.json': 'application/json',
            '.png': 'image/png',
            '.jpg': 'image/jpeg',
            '.svg': 'image/svg+xml'
        }
        
        suffix = file_path.suffix
        content_type = content_types.get(suffix, 'application/octet-stream')
        self.serve_file(file_path, content_type)

def open_browser(port):
    """打开浏览器"""
    import time
    time.sleep(1)
    webbrowser.open(f'http://localhost:{port}')

def main():
    """主函数"""
    port = int(os.environ.get('PORT', 8080))
    
    print("🍽️ Food Craft Server")
    print("=" * 50)
    print(f"📍 Local:   http://localhost:{port}")
    print(f"📍 Demo:    http://localhost:{port}/demo")
    print(f"📍 API:     http://localhost:{port}/api/stats")
    print("=" * 50)
    print("Press Ctrl+C to stop the server")
    print()
    
    # 自动打开浏览器
    threading.Thread(target=open_browser, args=(port,), daemon=True).start()
    
    # 启动服务器
    server = HTTPServer(('0.0.0.0', port), FoodCraftHandler)
    
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\n👋 Server stopped")
        server.server_close()

if __name__ == "__main__":
    main()
