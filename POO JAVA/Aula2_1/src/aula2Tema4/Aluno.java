package aula2Tema4;

public class Aluno {

	int matricula;
	String nome;
	String cpf;
			
	Aluno(int pMatricula, String pNome, String pCpf){
		matricula = pMatricula;
		nome = pNome;
		cpf = pCpf;
				
	}
	
	void info() {
		
		System.out.println("Matricula:" + matricula);
		System.out.println("Nome:" + nome);
		System.out.println("CPF:" + cpf); 
		System.out.println();
	}
}
	
