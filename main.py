from controller import Controller

def main():
    file_path, dp = Controller.get_info()
    Controller.run_app(file_path=file_path, is_optimized=dp)

if __name__ == "__main__":
    main()
