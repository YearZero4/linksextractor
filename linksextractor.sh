#!/bin/bash
chmod 777 *
#<<<<<<<<<<<<<<<<<<<<<<<<<< EXTRACTOR DE LINKS [PGX NOT-SECURE-SYSTEM] >>>>>>>>>>>>>>>>>>>>>>>>>
function linksextractor(){
clear && n=1
G="\033[1;32m" ; W="\033[1;37m"
file='index.html'
save='links.txt'
s='links_encontrados.txt'
echo -e "$W  _ _       _                  _                  _
 | (_)     | |                | |                | |
 | |_ _ __ | | _____  _____  _| |_ _ __ __ _  ___| |_ ___  _ __
 | | | '_ \\| |/ / __|/ _ \\ \\/ / __| '__/ _\` |/ __| __/ _ \\| '__|
 | | | | | |   <\__ \  __/>  <| |_| | | (_| | (__| || (_) | |
 |_|_|_| |_|_|\_\___/\___/_/\_\\__ |_|  \__,_|\___|\__\___/|_|
"
echo -e "$G"
for i in P G 'X ' N i n g u 'n ' S i s t e m 'a ' e 's ' S e g u r o . . .;do
echo -e -n "$i"
sleep 0.02
done ; echo -e "\n"

echo -e "
$G<<<[1]>>>$W EXTRAER LINKS PROPORCIONANDO UNA URL
$G<<<[2]>>>$W EXTRAER LINKS DE UN ARCHIVO
"

echo -e -n  "===> $G" ; read x
if [[ $x == 1 ]];then
echo -e -n "$W<<<LINK DEL SITIO WEB>>> $G"
read link
wget -q -O $file "$link"
elif [[ $x == 2 ]];then
echo -e -n "$W<<< EXTRAER LINKS DEL ARCHIVO>>> $G"
read fileO
file="$fileO"
else
echo -e "Opcion Invalida..." && sleep 3 ; linksextractor
fi
echo -e "\n"
cat $file | sed 's/ /\n/g' | grep -E "'|\"" | grep -Ei '^href|^src' | grep -v 'hreflang' \
| sed -n -e 's/.*"\(.*\)".*/\1/p' -e 's/.*'\''\(.*\)'\''.*$/\1/p' | sed 's/data://g' | sort | uniq>$save

cat $save | while read z;do
echo -e "$W[$n]$G $z"
((n=$n+1))
done>$s
rm $save

while read -r z; do
if [ ${#z} -gt $COLUMNS ]; then
z="${z:0:$(($COLUMNS - 3))}..."
fi
echo -e "$z"
done < "$s"

cat $s | grep 'http' | while read z;do echo -e "${z#* }\n";done>links.txt
rm "$s"

echo -e -n "\n[X]$W PARA FINALIZAR Y $G[ENTER]$W PARA CONTINUAR >>> "
read n
if [[ $n == "X" ]] || [[ $n == "x" ]];then
clear ; exit
else
linksextractor
fi
}
linksextractor
#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
