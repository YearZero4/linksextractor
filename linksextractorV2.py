while True:
 from colorama import Fore, init, Style
 from bs4 import BeautifulSoup as b
 import requests, os, sys, time, pyfiglet
 os.system('cls')
 found=[]
 init(autoreset=True)
 GREEN=f'{Fore.GREEN}{Style.BRIGHT}'
 WHITE=f'{Fore.WHITE}{Style.BRIGHT}'
 if os.path.exists('found_links.txt'):
  os.remove('found_links.txt')

 def extraer():
  banner=pyfiglet.figlet_format("Linksextractor")
  print(GREEN + banner)
  url=input(f'PONGA LA URL QUE DESEAS EXTRAER LINKS => {GREEN}')
  if url[0:8] != 'https://':
   url='https://' + url
  if url[-1:] != '/':
   url=url+'/'
  array1=['a', 'link', 'script', 'img']
  array2=['href', 'src']
  headers={
  'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; rv:134.0) Gecko/20100101 Firefox/134.0'
  }
  request=requests.get(url, headers=headers)
  soup=b(request.content, 'html.parser')
  for arr1 in array1:
   find_link=soup.find_all(arr1)
   for i in find_link:
    for arr2 in array2:
     try:
      found.append(f"{url}|{i[arr2]}")
     except:
      pass
 del_duplix=[]
 extraer()
 urls=[]
 for i in found:
  if i not in del_duplix:
   del_duplix.append(i)
 for d in del_duplix:
  zero=d.split('|')[0]
  one=d.split('|')[-1]
  bfind=one.find('www.')
  try:
   if one[0] != '/' or bfind == -1:
    if one[0] == '/':
     one=one[1:]
    url=zero+one
    url=url.replace('https://', '').split('//')[-1]
    if one[0:8] == 'https://':
     urls.append(one.replace('https://', ''))
    else:
     urls.append(url)
   else:
    if one[0:6] == '//www.':
     urls.append(one[6:])
    else:
     urls.append(one)
  except:
   pass

 all_links=[]
 all_links2=[]
 for url in enumerate(urls):
  n=f"{url[0]+1}" ; number=f"{str(n).zfill(2)}"
  link=f"[{number}] {url[1]}"
  link2=f"{GREEN}[{number}]{WHITE} {url[1]}"
  all_links.append(link)
  all_links2.append(link2)
 for i in all_links2:
  print(i)

 def save():
  for i in all_links:
   with open('found_links.txt', 'a') as f:
    f.write(f"{i}\n\n")
    f.close()
  print(f'\nDATOS GUARDADOS.')
  input('Presione [ENTER] Para Continuar...')
 n2=1
 x=input(f'\n{GREEN}[F] {WHITE}Buscar Alguna Palabra y mostrar resultados\n{GREEN}[G] {WHITE}PARA GENERAR TXT{GREEN}\n[X]{WHITE} PARA SALIR\n{GREEN}Enter Para Continuar...\n{WHITE}=====> ')

 if x == 'f' or x == 'F':
  if os.path.exists('found_links.txt'):
   os.remove('found_links.txt')
  palabra=input('Texto que deseas buscar => ')
  for i in all_links:
   find=i.find(palabra)
   if find != -1:
    sv=f"[{n2}] {i.split(']')[1]}"
    print(sv)
    with open('found_links.txt', 'a') as f:
     f.write(sv + '\n\n')
     f.close()
    n2+=1
  input('\nPresione [ENTER] Para Continuar...')
 elif x == 'g' or x == 'G':
  save()
 elif x == 'X' or x == 'x':
  print('\nHasta la proxima...')
  time.sleep(3)
  sys.exit()
 else:
  pass
