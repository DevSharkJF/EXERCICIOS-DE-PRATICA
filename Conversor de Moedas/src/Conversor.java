import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URI;
import java.util.Scanner;
import java.util.stream.Collectors;
import com.google.gson.JsonObject;
import com.google.gson.JsonParser;

public class Conversor {
    private static final String API_KEY = " ";
    private static final String API_URL = "https://v6.exchangerate-api.com/v6/" + API_KEY + "/latest/USD";
    private final Scanner scanner;

    public Conversor(Scanner scanner) {
        this.scanner = scanner;
    }

    public void converterMoeda(String de, String para) {
        try {
            double taxa = obterTaxaDeCambio(de, para);
            System.out.print("Digite o valor a ser convertido: ");
            double valor = lerValor();

            double resultado = valor * taxa;
            System.out.printf("%.2f %s = %.2f %s%n", valor, de, resultado, para);
        } catch (Exception e) {
            System.out.println("Erro ao converter: " + e.getMessage());
        }
    }

    private double obterTaxaDeCambio(String de, String para) throws IOException {
        HttpURLConnection conn = (HttpURLConnection) URI.create(API_URL).toURL().openConnection();
        conn.setRequestMethod("GET");

        if (conn.getResponseCode() != 200) {
            throw new RuntimeException("Erro: HTTP " + conn.getResponseCode());
        }

        BufferedReader reader = new BufferedReader(new InputStreamReader(conn.getInputStream()));
        String response = reader.lines().collect(Collectors.joining());
        reader.close();

        JsonObject jsonObject = JsonParser.parseString(response).getAsJsonObject();
        JsonObject taxas = jsonObject.getAsJsonObject("conversion_rates");

        double taxaDe = taxas.get(de).getAsDouble();
        double taxaPara = taxas.get(para).getAsDouble();
        return taxaPara / taxaDe;
    }

    private double lerValor() {
        while (!scanner.hasNextDouble()) {
            System.out.println("Digite um valor válido");
            scanner.next();
        }
        return scanner.nextDouble();
    }
}