import java.util.Scanner;

public class Banco {
    public static void main(String[] args) {
        String nome = "Gustavo";
        String conta = "Corrente";
        double saldo = 1500.00;

        System.out.println("");

        int opcao = 0;
        String menu = """
                ****************** BANCO SHARK🏦 ******************
                1 - Consultar Dados 👤
                2 - Depósito 💵
                3 - Sacar 💰
                4 - Sair ❌
                **************************************************
                """
                ;
        System.out.println("\n");

        while(opcao !=4){
            Scanner leitura = new Scanner(System.in);
            System.out.println(menu);
            System.out.print("Escolha uma das opções acima: ");
            opcao = leitura.nextInt();

            if (opcao == 1){
                System.out.println("Nome do Cliente: " + nome);
                System.out.println("Tipo de Conta: " + conta);
                System.out.println("Saldo Atual: " + saldo + "\n");

            } else if (opcao == 2) {
                System.out.println("Qual valor deseja depositar?");
                int valorDeposito = leitura.nextInt();
                saldo += valorDeposito;
                System.out.println("Seu novo saldo é de R$ " + saldo + "\n");

            } else if (opcao == 3) {
                System.out.println("Informe o valor a ser sacado:");
                double valorSaque = leitura.nextDouble();
                if(valorSaque > saldo){
                    System.out.println("⚠️AVISO⚠️\n");
                    System.out.println("Seu SALDO é MENOR do que valor de SAQUE\n");
                }else {
                    saldo -= valorSaque;
                    System.out.println("Novo saldo de R$ " + saldo + "\n");
                }
            } else if (opcao != 4) {
                System.out.println("⚠️O número informado é inválido❌");
            }
        }
    }
}