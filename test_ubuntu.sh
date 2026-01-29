#!/bin/bash

echo "=================================="
echo "Script de prueba para Ubuntu"
echo "Flask API - Pruebas Automatizadas"
echo "=================================="

# Colores para output
GREEN='\033[0;32m'
RED='\033[0;31m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Verificar Python
echo -e "\n${YELLOW}[1/5] Verificando Python...${NC}"
if command -v python3 &> /dev/null; then
    PYTHON_VERSION=$(python3 --version)
    echo -e "${GREEN}✓ $PYTHON_VERSION instalado${NC}"
else
    echo -e "${RED}✗ Python3 no está instalado${NC}"
    echo -e "${YELLOW}Instalar con: sudo apt-get install python3${NC}"
    exit 1
fi

# Verificar pip
echo -e "\n${YELLOW}[2/5] Verificando pip...${NC}"
if command -v pip3 &> /dev/null; then
    echo -e "${GREEN}✓ pip3 está instalado${NC}"
else
    echo -e "${RED}✗ pip3 no está instalado${NC}"
    echo -e "${YELLOW}Instalar con: sudo apt-get install python3-pip${NC}"
    exit 1
fi

# Instalar dependencias
echo -e "\n${YELLOW}[3/5] Instalando dependencias...${NC}"
pip3 install -r requirements.txt
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Dependencias instaladas correctamente${NC}"
else
    echo -e "${RED}✗ Error al instalar dependencias${NC}"
    exit 1
fi

# Ejecutar tests
echo -e "\n${YELLOW}[4/5] Ejecutando tests...${NC}"
python3 -m pytest tests/test_api.py -v
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Todos los tests pasaron correctamente${NC}"
else
    echo -e "${RED}✗ Algunos tests fallaron${NC}"
    exit 1
fi

# Ejecutar tests con cobertura
echo -e "\n${YELLOW}[5/5] Generando reporte de cobertura...${NC}"
python3 -m pytest tests/test_api.py --cov=app --cov-report=term --cov-report=html
if [ $? -eq 0 ]; then
    echo -e "${GREEN}✓ Reporte de cobertura generado${NC}"
    echo -e "${GREEN}  Ver reporte HTML en: htmlcov/index.html${NC}"
else
    echo -e "${RED}✗ Error al generar reporte de cobertura${NC}"
fi

# Preguntar si desea iniciar el servidor
echo -e "\n${YELLOW}¿Deseas iniciar el servidor Flask? (s/n)${NC}"
read -r response
if [[ "$response" =~ ^([sS][iI]|[sS])$ ]]; then
    echo -e "${GREEN}Iniciando servidor en http://localhost:5000${NC}"
    echo -e "${YELLOW}Presiona Ctrl+C para detener el servidor${NC}"
    python3 -m app.app
fi

echo -e "\n${GREEN}=================================="
echo "✓ Proceso completado exitosamente"
echo "==================================${NC}"
