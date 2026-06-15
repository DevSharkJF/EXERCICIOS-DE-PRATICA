import java.util.Scanner;
/* Escrever um programa que leia o número de identificação, as 3 notas obtidas por um
aluno nas 3 verificações e a média dos exercícios que fazem parte da avaliação. Valide
para que todas as entradas sejam 0 ≤ nota ≤ 10. Calcule a média de aproveitamento do
aluno, usando a fórmula: media = ((nota1 + nota2 + nota3 *3) + media dos exercicios)/7 
Média de Aproveitamento Conceito
>= 9.0 e <= 10  A
>= 7.5 e < 9.0  B
>= 6.0 e < 7.5  C
>= 4.0 e < 6.0  D
        < 4.0 	E
𝑀é𝑑𝑖𝑎 = (𝑛𝑜𝑡𝑎1 + 𝑛𝑜𝑡𝑎2 ∗ 2 + 𝑛𝑜𝑡𝑎3 ∗ 3 + 𝑚𝑒𝑑𝑖𝑎 𝑑𝑜𝑠 𝑒𝑥𝑒𝑟𝑐𝑖𝑐𝑖𝑜𝑠) / 7  
*/

public class exercicio5 {

	public static void main(String[] args) {
		Scanner input = new Scanner(System.in);

		double[] notas = new double[3];
		double mediaExercicios = 0.0;
		int i;
		double media = 0.0;
		double mediaFinal = 0.0; // = (𝑛𝑜𝑡𝑎1 + 𝑛𝑜𝑡𝑎2 ∗ 2 + 𝑛𝑜𝑡𝑎3 ∗ 3 + 𝑚𝑒𝑑𝑖𝑎 𝑑𝑜𝑠 𝑒𝑥𝑒𝑟𝑐𝑖𝑐𝑖𝑜𝑠) / 7;
		char opc = 's';
		char aproveitamento = ' ';
		String resposta = " ";
		
		System.out.println("Programa que calcula a media das notas de um aluno: ");

		do {

			for (i = 0; i <= 2; i++) {
				System.out.printf("Digite a %d nota do aluno:", i + 1);
				notas[i] = input.nextDouble();
				media = (notas[0] + notas[1] * 2) + (notas[2] * 3);
			
			}
			
			System.out.println("Entre com o valor das notas dos exercicios");
			mediaExercicios = input.nextDouble();

			mediaFinal = (media + mediaExercicios) / 7;
			
			if(mediaFinal > 9.0) {
				aproveitamento = 'A';
			}else if(mediaFinal >= 7.5) {
				aproveitamento = 'B';
			}else if (mediaFinal >= 6.0) {
				aproveitamento = 'C';
			}else if (mediaFinal >= 4) {
				aproveitamento = 'D';
			}else {
				aproveitamento = 'E';
			}
			
			switch (aproveitamento) {
			case 'A':
				resposta = "aprovado";
				break;
			case 'B':
				resposta = "aprovado";
				break;
			case 'C':
				resposta = "aprovado";
				break;
			case 'D':
				resposta = "reprovado";
				break;
			case 'E':
				resposta = "reprovado";
				break;
			}

			System.out.printf("Deseja continuar? %n[Sim/nao] ");
			opc = input.next().charAt(0);
		} while (opc != 'n');

		System.out.printf("A media das notas foi %.2f %nMedia de exercicios %.2f %nMedia final = %.2f com um aproveitamento %s voce esta %s", media ,mediaExercicios, mediaFinal, aproveitamento,resposta);
	}
}