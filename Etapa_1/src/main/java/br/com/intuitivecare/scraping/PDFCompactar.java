package src.main.java.br.com.intuitivecare.scraping;

import java.io.FileOutputStream;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.nio.file.Path;
import java.util.List;
import java.util.zip.ZipEntry;
import java.util.zip.ZipOutputStream;

public class PDFCompactar {
    public void compactar(List<String> arquivos, String zipSaida) throws IOException {
        Path zipFilePath = Paths.get(zipSaida);
        Files.createDirectories(zipFilePath.getParent());

        try (ZipOutputStream zipOut = new ZipOutputStream(new FileOutputStream(zipSaida))) {
            for (String arquivo : arquivos) {
                Path filePath = Paths.get("Etapa_1/src/main/output/anexos", arquivo);

                if (Files.exists(filePath)) {
                    Path fileName = filePath.getFileName();
                    zipOut.putNextEntry(new ZipEntry(fileName.toString()));
                    Files.copy(filePath, zipOut);
                } else {
                    System.err.println("O arquivo '" + arquivo + "' não foi encontrado no diretório: " + filePath);
                }
            }
        } catch (IOException e) {
            System.err.println("Erro ao compactar os arquivos no ZIP: " + e.getMessage());
            throw e;
        }
    }
}