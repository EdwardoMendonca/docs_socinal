from interga_dev import create_app

app = create_app()

# Inicia a aplicação ------------------------------
if __name__ == '__main__':
  app.run(debug=True)
  # app.run()
  # app.run(host='0.0.0.0', port=5000, debug=True)
