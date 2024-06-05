vscode_files = {
    "settings.json": """{
    "python.pythonPath": "${workspaceFolder}/venv/bin/python",
    "editor.formatOnSave": true,
    "editor.codeActionsOnSave": {
        "source.organizeImports": true,
        "source.fixAll": true
    },
    "python.linting.enabled": true,
    "python.linting.ruffEnabled": true,
    "python.formatting.provider": "black"
}""",
    "keybindings.json": """[
    {
        "key": "ctrl+shift+b",
        "command": "workbench.action.tasks.build",
        "when": "editorTextFocus"
    }
]""",
    "snippets.json": """{
    "Print to console": {
        "prefix": "log",
        "body": [
            "console.log('$1');",
            "$2"
        ],
        "description": "Log output to console"
    }
}""",
}
