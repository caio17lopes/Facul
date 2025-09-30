package IMC;

import java.util.Scanner;

public class Exercicios {

	public static void main(String[] args) {
		
		int peso;
		double altura; 
		Scanner teclado = new Scanner (System.in);
		
		System.out.println("Digite seu peso");
		peso = teclado.nextInt();
		System.out.println("Digite sua altura");
		altura = teclado.nextDouble();
		
		double imc = peso / (altura*altura);
		
		System.out.printf("Seu IMC é %.2f ", imc);
		
		
		
		
	}

}
