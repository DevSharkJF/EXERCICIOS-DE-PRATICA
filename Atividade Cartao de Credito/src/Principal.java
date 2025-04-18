import java.util.ArrayList;
import java.util.Collections;
import java.util.Scanner;

public class Principal {
    public static void main(String[] args) {
        int opcao = 0;
        String menu = """
                \n
                **************************************************
                Sistema de Cartão de Crédito
                1 - Inserir Compra
                2 - Ver Compras
                3 - Sair
                **************************************************
                """;

        System.out.println("\n");

        Scanner leitura = new Scanner(System.in);
        CartaoDeCredito cartao = null;

        while (opcao != 3) {
            System.out.println(menu);
            System.out.print("Escolha uma opção: ");
            opcao = leitura.nextInt();
            leitura.nextLine(); 

            if (opcao == 1) {
                if (cartao == null) {
                    System.out.print("Digite o limite do cartão: ");
                    double limite = leitura.nextDouble();
                    leitura.nextLine(); 
                    cartao = new CartaoDeCredito(limite);
                }

                System.out.print("Digite a descrição da compra: ");
                String descricao = leitura.nextLine();

                System.out.print("Digite o valor da compra: ");
                double valor = leitura.nextDouble();
                leitura.nextLine();

                Compra compra = new Compra(descricao, valor);
                boolean compraRealizada = cartao.lancaCompra(compra);
                if (compraRealizada) {
                    System.out.println("Compra realizada!");
                    System.out.println("\nSaldo do cartão: " + cartao.getSaldo());
                } else {
                    System.out.println("Saldo insuficiente!");
                }

            } else if (opcao == 2) {
                System.out.println("***********************");
                if (cartao != null) {
                    System.out.println("COMPRAS REALIZADAS:\n");
                    Collections.sort(cartao.getCompras());
                    for (Compra c : cartao.getCompras()) {
                        System.out.println(c.getDescricao() + " - " + c.getValor());
                    }
                    System.out.println("\n***********************");
                    System.out.println("\nSaldo do cartão: " + cartao.getSaldo());
                } else {
                    System.out.println("Nenhuma compra foi realizada.");
                }

            } else if (opcao == 3) {
                System.out.println("Sistema encerrado!");
            } else{
                System.out.println("Opção inválida! Tente novamente.");
            }
        }
        leitura.close();
    }
}
