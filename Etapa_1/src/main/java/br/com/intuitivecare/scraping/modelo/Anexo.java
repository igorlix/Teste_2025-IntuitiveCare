package br.com.intuitivecare.scraping.modelo;

public class Anexo {
    private String nome;
    private String url;

    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        if (nome == null || nome.trim().isEmpty()) {
            throw new IllegalArgumentException("O nome não pode ser nulo ou vazio");
        }
        this.nome = nome;
    }

    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        if (url == null || url.trim().isEmpty()) {
            throw new IllegalArgumentException("A URL não pode ser nula ou vazia");
        }
        this.url = url;
    }
}