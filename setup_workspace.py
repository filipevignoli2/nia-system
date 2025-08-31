import os

# Estrutura de diretórios a ser criada
STRUCTURE = {
    "backend": {
        "app": {
            "api": ["protocols.py", "operators.py", "dashboard.py", "upload.py", "monitoring.py"],
            "models": ["protocol.py", "operator.py", "base.py", "enums.py"],
            "services": ["protocol_service.py", "operator_service.py", "upload_service.py", "dashboard_service.py", "distribution_service.py"],
            "utils": ["database.py", "validators.py", "decorators.py", "exceptions.py", "helpers.py"],
            "socket": ["chat_handlers.py", "events.py"],
            "__init__.py": "",
            "config.py": "",
            "extensions.py": ""
        },
        "migrations": {},
        "tests": ["test_api.py", "test_services.py", "test_models.py"],
        "requirements.txt": "",
        "run.py": ""
    },
    "frontend": {
        "public": ["index.html"],
        "src": {
            "components": {
                "common": ["Header.jsx", "Sidebar.jsx", "Loading.jsx", "ErrorBoundary.jsx", "ConfirmDialog.jsx"],
                "forms": ["FormField.jsx", "FormSelect.jsx", "FormInput.jsx", "FormTextarea.jsx"],
                "tables": ["DataTable.jsx", "TablePagination.jsx", "FilterDropdown.jsx", "StatusIndicator.jsx"],
                "modals": ["BaseModal.jsx", "DetailsModal.jsx"]
            },
            "pages": {
                "dashboard": {
                    "components": ["KPICards.jsx", "SLAChart.jsx", "SpecialtyChart.jsx", "ForecastChart.jsx", "MonthlyDemandChart.jsx", "ProductivityChart.jsx"],
                    "hooks": ["useDashboardData.js"],
                    "DashboardPage.jsx": ""
                },
                "protocols": {
                    "components": ["ProtocolTable.jsx", "ProtocolFilters.jsx", "ProtocolStatusCell.jsx", "ProtocolActions.jsx"],
                    "hooks": ["useProtocols.js", "useProtocolFilters.js"],
                    "ProtocolsPage.jsx": ""
                },
                "monitoring": {
                    "components": ["MonitoringTable.jsx", "DeadlineIndicator.jsx"],
                    "hooks": ["useMonitoring.js"],
                    "MonitoringPage.jsx": ""
                },
                "admin": {
                    "components": ["OperatorManager.jsx", "OperatorForm.jsx", "OperatorTable.jsx", "DemandReallocation.jsx"],
                    "hooks": ["useOperators.js", "useDemandReallocation.js"],
                    "AdminPage.jsx": ""
                },
                "upload": {
                    "components": ["FileUploader.jsx", "UploadProgress.jsx", "UploadHistory.jsx"],
                    "hooks": ["useFileUpload.js"],
                    "UploadPage.jsx": ""
                },
                "chat": {
                    "components": ["ChatWindow.jsx", "MessageList.jsx", "MessageInput.jsx", "UserList.jsx", "RoomTabs.jsx", "NotificationBadge.jsx"],
                    "hooks": ["useChat.js", "useSocket.js", "useNotifications.js"],
                    "ChatPage.jsx": ""
                }
            },
            "services": {
                "api": ["apiClient.js", "protocols.js", "operators.js", "dashboard.js", "upload.js", "chat.js"],
                "socket": ["socketService.js"],
                "utils": ["dateUtils.js", "formatUtils.js", "validationUtils.js", "constants.js"]
            },
            "hooks": ["useAuth.js", "useLocalStorage.js", "useDebounce.js", "useAsyncOperation.js"],
            "context": ["AuthContext.jsx", "NotificationContext.jsx", "ThemeContext.jsx"],
            "styles": ["globals.css", "components.css", "variables.css"],
            "App.jsx": "",
            "index.js": "",
            "setupTests.js": ""
        },
        "package.json": "",
        "README.md": ""
    },
    "database": {
        "migrations": {},
        "seeds": {},
        "schema.sql": ""
    },
    "docs": ["API.md", "DEPLOYMENT.md", "DEVELOPMENT.md", "ARCHITECTURE.md"],
    "scripts": ["deploy.sh", "backup.sh", "setup.sh"],
    "docker-compose.yml": "",
    ".gitignore": "",
    ".env.example": "",
    "README.md": ""
}

def create_structure(base_path, structure):
    """
    Cria recursivamente a estrutura de diretórios e arquivos.
    """
    for name, content in structure.items():
        path = os.path.join(base_path, name)
        if isinstance(content, dict):
            # É um diretório
            os.makedirs(path, exist_ok=True)
            # Adiciona __init__.py se for um pacote Python
            if any(f.endswith('.py') for f in content.keys()):
                 open(os.path.join(path, '__init__.py'), 'a').close()
            create_structure(path, content)
        elif isinstance(content, list):
             # É um diretório com uma lista de arquivos
            os.makedirs(path, exist_ok=True)
            if any(f.endswith('.py') for f in content):
                 open(os.path.join(path, '__init__.py'), 'a').close()
            for filename in content:
                open(os.path.join(path, filename), 'a').close()
        else:
            # É um arquivo
            open(path, 'a').close()

if __name__ == "__main__":
    print("Criando a estrutura de diretórios do projeto nia-system...")
    create_structure('.', STRUCTURE)
    print("Estrutura criada com sucesso!")
