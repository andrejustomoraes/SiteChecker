import requests


def main():
  urls = []
  print("insira um site para verificar, para varios sites, divida com vírgula:")
  urls = str(input()).lower().split(",")

#list of ports to check
  http_actives = [200, 202, 204 , 301, 302, 303, 404 ]

  
  #browse the sites
  for url in urls:
    url = url.strip()

    #verifica se a url contém ponto
  if "." not in url:
    print( url, " url invalida, adicione ponto")
  else:
  
    #add https if there is no http or https
    if "http" not in url:
      url = f"https://{url}"

  #test the url passed by the user
  try:
    requisition = requests.get(url)
    if requisition.status_code in http_actives:
      print(url, "site online")
    else:
      print(url, "site offline")
  except:
    print (url, "erro")
  menu()


# interactive user menu
def menu():
  choice = str(input("Verificar mais um site? s/n")).lower()
  if choice == "s":
    main()
  elif choice == "n":
    print("até mais...")
  else:
    print("opção inválida")
    menu()


main()