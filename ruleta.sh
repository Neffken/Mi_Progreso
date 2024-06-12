#!/bin/bash

#Colours
greenColour="\e[0;32m\033[1m"
endColour="\033[0m\e[0m"
redColour="\e[0;31m\033[1m"
blueColour="\e[0;34m\033[1m"
yellowColour="\e[0;33m\033[1m"
purpleColour="\e[0;35m\033[1m"
turquoiseColour="\e[0;36m\033[1m"
grayColour="\e[0;37m\033[1m"

function helpPanel(){
    echo -e "\n${yellowColour}[+] ${endColour}${blueColour} Uso: ${endColour}\n"
    echo -e "\t-m) Dinero con el que desea jugar"
    echo -e "\t-t) Tecnica al utilizar (martingala/inverseLabrouchere\n"
    exit 1
}

function ctrl_c(){
	echo -e "\n\n[!] Saliendo..."
	tput cnorm; exit 1
}

function martingala(){
	echo -e "\n [+] Dinero actual: $money€"
    echo -n "[+] ¿Cuanto dinero tienes pensado apostar? -> " && read initial_bet
    echo -n "[+] ¿A qué deseas apostar continuamente (par/impar)? -> " && read par_impar

    echo "[+] Vamos a jugar con una cantidad inicial de $initial_bet€ a $par_impar"
	backup_bet=$initial_beat
	play_counter=1
	jugadas_malas="[ "
	jugadas_buenas="[ "
	tput civis
	while true; do
		money=$((money-$initial_bet))
		#echo -e "\n[+] Acabas de apostar $initial_bet y tienes $money€"
		random_number="$(($RANDOM % 37))"
		#echo -e "\n${yellowColour}[+]${endColour} Ha salido el numero ${blueColour}$random_number${endColour}"

		if [ ! "$money" -le 0 ]; then

			if [ "$par_impar" == "par" ]; then
				if [ "$((random_number % 2))" -eq 0 ]; then
					if [ "$random_number" -eq 0 ]; then
		#				echo "[+] Ha salido el 0, por tanto perdemos"
						 initial_bet=$(($initial_bet*2))
						 jugadas_malas+="$random_number "
						# jugadas_buenas=""
                    #	echo -e "[+] Ahora mismo tienes $money€"
					else
					#	echo -e "[+]${greenColour} El número que ha salido es par !Ganas${endColour}"
						reward=$((initial_bet*2))
					#	echo "[!] Ganas un total de $reward€"
						money=$(($money+$reward))
						jugadas_malas=""
						jugadas_buenas+="$random_number "
					#	echo "[+] Tienes $money"
					fi
				else
					#echo -e "[+] ${redColour}El número que a salido es impar !Pierdes{endColour}"
					initial_bet=$(($initial_bet*2))
					jugadas_malas+="$random_number "
					#echo -e "[+] Ahora mismo tienes $money€"
					
				fi
			fi	
		else
			# Nos quedamos sin plata
			echo -e "\n${redColour} [!] Te haz quedado sin plata${endColour}"
			echo -e "${yellowColour}[+]${endColour} Han habido un total de ${redColour}$play_counter${endColour} jugadas"
            echo -e "${yellowColour}[!]${endColour} ${redColour} A continuacion se mostraran las jugadas consecutivas malas${endcolour}"
            echo -e "${blueColour}$jugadas_malas${endColour}"
			echo -e "\nSe mostraran las jugadas buenas\n"
            echo -e "${blueColour}$jugadas_buenas${endColour} y haz ganado un total de: ${yellowColour}$reward${endColour} "

			tput cnorm; exit 0
		fi
		let play_counter+=1		
	done		
}

# Ctrl C
trap ctrl_c INT

while getopts "m:t:h" arg; do
    case $arg in
    	m) money=$OPTARG;;
    	t) technique=$OPTARG;;
        h) helpPanel;;
    esac
done

if [ $money ] && [ $technique ]; then
	if [ $technique == "martingala" ]; then
	martingala
	else
		echo -e "\n [!] La tecnica utilizada no se encuentra\n"
		helpPanel
	fi
else
    helpPanel
fi
