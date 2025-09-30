package Exercicio2;

import java.util.Scanner;

public class Atividade2 {

	public static void main(String[] args) {
		Scanner teclado = new Scanner (System.in);
		
		int palpite;
		int valorCorreto = 10000;
		
		System.out.println("Digite seu palpite");
		palpite = teclado.nextInt();
		String msg; //operador ternario
		
		while(palpite != valorCorreto) {
			msg = palpite>valorCorreto? "Um pouco menos...":"Um pouco menos...";
			
			/*if (palpite > valorCorreto) {
				System.out.println("Um pouco menos....");
			}
			else {
				System.out.println("Um pouco mais");
			}
			*/
			System.out.println("Digite outro palpite");
			palpite = teclado.nextInt();
			
		}
		
		System.out.println("Parabéns você acertou!");
	}
}
