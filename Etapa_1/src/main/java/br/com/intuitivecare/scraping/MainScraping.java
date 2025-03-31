package src.main.java.br.com.intuitivecare.scraping;

import br.com.intuitivecare.scraping.modelo.Anexo;

import java.io.IOException;
import java.util.List;
import java.util.stream.Collectors;

public class MainScraping {
    public static void main(String[] args) {
        PDFBaixar baixa = new PDFBaixar();
        PDFCompactar compacta = new PDFCompactar();

        try {
            List<Anexo> anexos = baixa.buscarAnexos("https://www.gov.br/ans/pt-br/acesso-a-informacao/participacao-da-sociedade/atualizacao-do-rol-de-procedimentos");

            if (anexos.isEmpty()) {
                System.err.println("Nenhum PDF relevante (Anexo I ou Anexo II) foi encontrado na página.");
                return;
            }

            anexos.forEach(anexo -> {
                try {
                    baixa.baixarPDF(anexo, "Etapas_1_2/src/main/output/anexos/");
                } catch (IOException e) {
                    System.err.println("Erro ao baixar o PDF: " + anexo.getUrl());
                    e.printStackTrace();
                }
            });

            compacta.compactar(
                    anexos.stream().map(Anexo::getNome).collect(Collectors.toList()),
                    "Etapas_1_2/src/main/output/Anexos.zip"
            );

            System.out.println("Processo concluído! Arquivo compactado criado em: output/Anexos.zip");

        } catch (IOException e) {
            System.err.println("Erro geral no processo: " + e.getMessage());
            e.printStackTrace();
        }
    }
}