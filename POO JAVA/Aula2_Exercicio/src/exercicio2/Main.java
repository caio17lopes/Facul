package exercicio2;

public class Main {

	public static void main(String[] args) {
		
		Aluno a1 = new Aluno("Caio","Informatica", new Avaliacao(9,10,6));
		Aluno a2 = new Aluno("Matheus","Informatica", new Avaliacao(8,7,6));
		
		
		a1.info();
		a2.info();
		
	}

}
