import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        Menu menu = new Menu(scanner);
        Conversor conversor = new Conversor(scanner);

        boolean continuar = true;
        while (continuar) {
            menu.exibirMenu();
            int opcao = menu.lerOpcao();

            if (opcao == 7) {
                continuar = false;
                System.out.println("Programa Finalizado!");
            } else if (opcao >= 1 && opcao <= 6) {
                String[] moedas = menu.obterMoedas(opcao);
                conversor.converterMoeda(moedas[0], moedas[1]);
            } else {
                System.out.println("Opção inválida, por favor tente novamente!");
            }
        }
        scanner.close();
    }
}