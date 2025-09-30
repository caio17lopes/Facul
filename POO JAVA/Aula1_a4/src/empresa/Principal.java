package empresa;

import java.util.Scanner;

public class Principal {

	public static void main(String[] args) {
		
		int idade;
		float peso; 
		
		Scanner teclado = new Scanner(System.in);
		System.out.println("Digite sua idade");
		idade = teclado.nextInt();
		System.out.println("Digite seu peso");
		peso = teclado.nextFloat();
		System.out.println("Digite seu nome");
		String nome = teclado.next();
		
		System.out.println("Nome: " + nome);
		
		System.out.printf("Peso: %.2f\n",peso);
		
		System.out.println("Idade: " + idade);
		
		System.out.println("Hello World");
// println da espaço o print imprimi tudo na mesma linha 
		if (idade <18) {
			System.out.println("Acesso bloqueado");
		}
		else if (idade < 65) {
			System.out.println("Adulto");
		
		}	
		else {
			System.out.println("Idoso");
		}
		
		for (int i=0; i<11; i++) {
			System.out.println("Valor: "+i);
		}
		// array
		int megaSena []= {11,14,21,30,06,44,56};
		// criar ele vazio int numeros[] = new int[200] criei com 200 numeros
		megaSena[0] = 10;
	}
	
	
	
}


