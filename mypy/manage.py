# 入口文件
# from app import create_app

# app = create_app('default')

from app import user

def main():
  user.run()

if __name__ == "__main__":
  main()