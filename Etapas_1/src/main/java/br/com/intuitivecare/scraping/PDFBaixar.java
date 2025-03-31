package src.main.java.br.com.intuitivecare.scraping;

import br.com.intuitivecare.scraping.modelo.Anexo;
import org.jsoup.Jsoup;
import org.jsoup.nodes.Document;
import org.jsoup.select.Elements;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.util.List;
import java.util.stream.Collectors;

public class PDFBaixar {

    public List<Anexo> buscarAnexos(String url) throws IOException {
        Document doc = Jsoup.connect(url).get();
        Elements links = doc.select("a[href$=.pdf]");

        System.out.println("Total de PDFs encontrados na página: " + links.size());

        return links.stream()
                .filter(link -> link.text().contains("Anexo I") || link.text().contains("Anexo II"))
                .map(link -> {
                    String href = link.attr("abs:href");
                    String nomeArquivo = href.substring(href.lastIndexOf('/') + 1).trim();

                    Anexo anexo = new Anexo();
                    anexo.setNome(nomeArquivo);
                    anexo.setUrl(href);
                    return anexo;
                })
                .collect(Collectors.toList());
    }

    public void baixarPDF(Anexo anexo, String diretorio) throws IOException {

        Files.createDirectories(Paths.get(diretorio));

        try {
            URL url = new URL(anexo.getUrl());
            HttpURLConnection connection = (HttpURLConnection) url.openConnection();
            connection.setRequestMethod("GET");
            connection.setConnectTimeout(20000);
            connection.setReadTimeout(30000);
            int responseCode = connection.getResponseCode();

            if (responseCode == HttpURLConnection.HTTP_OK) {
                int fileSize = connection.getContentLength();
                int progress = 0;

                try (InputStream in = connection.getInputStream();
                     FileOutputStream out = new FileOutputStream(diretorio + anexo.getNome())) {

                    byte[] buffer = new byte[8192];
                    int bytesRead;

                    while ((bytesRead = in.read(buffer)) != -1) {
                        out.write(buffer, 0, bytesRead);
                        progress += bytesRead;

                        if (fileSize > 0) {
                            int percentCompleted = (int) ((progress / (double) fileSize) * 100);
                            System.out.print("\rDownload de " + anexo.getNome() + ": " + percentCompleted + "%");
                        }
                    }
                    System.out.println();
                    System.out.println("Arquivo baixado com sucesso: " + anexo.getNome());
                }
            } else {
                System.err.println("Falha ao baixar o arquivo: " + anexo.getUrl() +
                        " (Código HTTP: " + responseCode + ")");
            }
        } catch (IOException e) {
            System.err.println("Erro ao fazer download de: " + anexo.getUrl());
            throw e;
        }
    }
}