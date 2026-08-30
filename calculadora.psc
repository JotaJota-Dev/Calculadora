Algoritmo calculadora
	Definir n1, n2, opc, contador, intentos Como Entero
	contador = 0
	intentos = 5
	
	
	Repetir
		Escribir "                           ============MENU==============                     "
		Escribir "Elige una de las siguientes 5 opciones: "
		Escribir "1. Suma"
		Escribir "2. Resta"
		Escribir "3. Multiplicación"
		Escribir "4. División"
		Escribir "5. Salir"
		Escribir "                          ¡ADVERTENCIA!                                "
		ESCRIBIR "SOLO TIENES 5 INTENTOS"
		ESCRIBIR "NO DESPERDICIES INTENTOS INGRESANDO NUMEROS MENORES QUE 1 Y MAYORES QUE 5 PORQUE GASTAN INTENTOS"
		Leer opc; 
		
		
		Segun opc hacer 
			
			1: 
				Escribir "Introduce el valor del primer número: ";
				Leer n1;
				escribir "Introduce el valor del segundo numero: ";
				Leer n2;
				Escribir "El resultado de la suma de los dos números es: ", (n1 + n2);
				contador = contador + 1;
				Escribir "Este es tu intento número ", contador, " te quedan ", (intentos - contador);
				
			2: 
				Escribir "Introduce el valor del primer número: ";
				Leer n1;
				escribir "Introduce el valor del segundo numero: ";
				Leer n2;
				Escribir "El resultado de la resta de los dos números es: ", (n1 - n2);
				contador = contador + 1; 
				Escribir "Este es tu intento número ", contador, " te quedan ", (intentos - contador);

			3: 
				Escribir "Introduce el valor del primer número: ";
				Leer n1;
				escribir "Introduce el valor del segundo numero: ";
				Leer n2;
				Escribir "El resultado de la multiplicación de los dos números es: ", (n1 * n2);
				contador = contador + 1
				Escribir "Este es tu intento número ", contador, " te quedan ", (intentos - contador);

			4: 
				Escribir "Introduce el valor del primer número: ";
				Leer n1;
				escribir "Introduce el valor del segundo numero: ";
				Leer n2;
				Escribir "El resultado de la división de los dos números es: ", (n1 / n2);
				contador = contador + 1
				Escribir "Este es tu intento número ", contador, " te quedan ", (intentos - contador);

			5:
				ESCRIBIR "¡ADIÓS!"
			de otro modo:
				Escribir "ERROR: ¡Valor introducido no valido!";
				Escribir "Advertencia: NO introducir valores menores de 1 y mayores que 5"
				contador = contador + 1;
				Escribir "EL número ingresado no está entre las opciones aún así este es tu intento número ", contador, " te quedan ", (intentos - contador), ", no vuelvas a desperciar otro intento";

				
		FinSegun
		
		si contador = 5 Entonces
			escribir "Agotado número de intentos"
		FinSi
		
	Hasta Que opc = 5 o contador >= 5
	

FinAlgoritmo