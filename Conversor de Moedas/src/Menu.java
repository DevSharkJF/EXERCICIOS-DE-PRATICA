import java.util.Scanner;

public class Menu {
    private final Scanner scanner;

    public Menu(Scanner scanner) {
        this.scanner = scanner;
    }

    public void exibirMenu() {
        System.out.println("\n*************************************\n");
        System.out.println("Bem vindo ao Conversor de Moedas\n");
        System.out.print("""
            1) Real -> Dólar
            2) Real -> Peso argentino
            3) Real -> Euro
            4) Dólar -> Real
            5) Peso argentino -> Real
            6) Euro -> Real
            7) Sair
            Escolha uma opção:\s"""
        );
    }

    public int lerOpcao() {
        while (!scanner.hasNextInt()) {
            System.out.println("Opção inválida. Tente novamente.");
            scanner.next();
        }
        return scanner.nextInt();
    }

    public String[] obterMoedas(int opcao) {
        switch (opcao) {
            case 1: return new String[]{"BRL", "USD"};
            case 2: return new String[]{"BRL", "ARS"};
            case 3: return new String[]{"BRL", "EUR"};
            case 4: return new String[]{"USD", "BRL"};
            case 5: return new String[]{"ARS", "BRL"};
            case 6: return new String[]{"EUR", "BRL"};
            default: throw new IllegalArgumentException("Opção inválida");
        }
    }
}
