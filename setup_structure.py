import pathlib

def create_project_structure():
    # Definir el directorio base
    base_dir = pathlib.Path("lead_mining_engine")
    
    # Lista de directorios a crear
    directories = [
        "data/inputs",
        "data/outputs",
        "data/temp",
        "data/logs",
        "preprocessing",
        "sunat",
        "tacto",
        "validation",
        "exports",
        "shared",
        "tests"
    ]

    # Diccionario con los archivos a crear en cada directorio
    files = {
        "preprocessing": ["split_rucs.py", "dni_extractor.py", "district_classifier.py", "cleaner.py", "__init__.py"],
        "sunat": ["sunat_scraper.py", "representative_parser.py", "captcha_handler.py", "__init__.py"],
        "tacto": ["tacto_scraper.py", "session_manager.py", "phone_parser.py", "__init__.py"],
        "validation": ["osiptel_validator.py", "phone_cleaner.py", "__init__.py"],
        "exports": ["excel_exporter.py", "__init__.py"],
        "shared": ["base_scraper.py", "logger.py", "utils.py", "config.py", "__init__.py"],
        "tests": ["__init__.py"],
        "": ["main.py", "requirements.txt", "Dockerfile", "docker-compose.yml", ".env"] # Raíz del proyecto
    }

    # 1. Crear directorios
    print("Creando directorios...")
    for directory in directories:
        dir_path = base_dir / directory
        dir_path.mkdir(parents=True, exist_ok=True)
        print(f"📁 Directorio creado: {dir_path}")

    # 2. Crear archivos
    print("\nCreando archivos...")
    for folder, filenames in files.items():
        for filename in filenames:
            file_path = base_dir / folder / filename
            file_path.touch(exist_ok=True)
            print(f"📄 Archivo creado: {file_path}")

if __name__ == "__main__":
    create_project_structure()
    print("\n🚀 ¡Estructura del proyecto Lead Mining Engine generada con éxito!")