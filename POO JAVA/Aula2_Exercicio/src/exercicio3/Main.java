package exercicio3;

public class Main {

	public static void main(String[] args) {
		Conta c1 = new Conta(001,"Caio", 2000,500);
		
		c1.info();
		
		 if(!c1.sacar(200)) {
			 System.out.println("Erro ao fazer o saque");
		 }
		 
		if(!c1.depositar(500)) {
			System.out.println("Erro ao depositar");
		}
		System.out.println();
		c1.info();
		
		

	}

}
