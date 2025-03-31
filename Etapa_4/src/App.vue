<template>
  <div class="search-container">
    <SearchHeader />

    <SearchControls
        :search-query="searchQuery"
        :filters="filters"
        :estados="estados"
        :modalidades="modalidades"
        @update:searchQuery="val => searchQuery = val"
        @update:filters="val => filters = val"
        @search="performSearch"
    />

    <SearchResults
        :results="results"
        :count="count"
        :isLoading="isLoading"
        :error="error"
        :searchPerformed="searchPerformed"
        @export="exportToCSV"
        @reset="resetFilters"
        @format-cnpj="formatCNPJ"
        @format-date="formatDate"
        @format-cep="formatCEP"
    />
  </div>
</template>

<script>
import axios from 'axios';
import SearchHeader from '@/components/SearchHeader.vue';
import SearchControls from '@/components/SearchControls.vue';
import SearchResults from '@/components/SearchResults.vue';

export default {
  name: 'SearchOperadoras',
  components: {
    SearchHeader,
    SearchControls,
    SearchResults
  },
  data() {
    return {
      searchQuery: '',
      filters: {
        cidade: '',
        uf: '',
        modalidade: ''
      },
      estados: [
        'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA',
        'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN',
        'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
      ],
      modalidades: [
        'Seguradora Especializada em Saúde',
        'Cooperativa Médica',
        'Cooperativa Odontológica',
        'Odontologia de Grupo',
        'Medicina de Grupo',
        'Autogestão',
        'Filantropia'
      ],
      results: [],
      count: 0,
      isLoading: false,
      error: null,
      searchPerformed: false
    };
  },
  methods: {
    async performSearch() {
      if (!this.searchQuery.trim() && !this.filters.cidade && !this.filters.uf && !this.filters.modalidade) {
        this.error = 'Informe ao menos um critério de busca (nome, cidade, UF ou modalidade)';
        return;
      }

      this.isLoading = true;
      this.error = null;
      this.results = [];
      this.count = 0;
      this.searchPerformed = true;

      try {
        let queryParams = `q=${encodeURIComponent(this.searchQuery)}`;

        if (this.filters.cidade) {
          queryParams += `&cidade=${encodeURIComponent(this.filters.cidade)}`;
        }

        if (this.filters.uf) {
          queryParams += `&uf=${encodeURIComponent(this.filters.uf)}`;
        }

        if (this.filters.modalidade) {
          queryParams += `&modalidade=${encodeURIComponent(this.filters.modalidade)}`;
        }

        const response = await axios.get(
            `http://192.168.0.14:8000/api/operadoras?${queryParams}`
        );

        if (response.data.success) {
          this.results = response.data.results;
          this.count = response.data.count;
        } else {
          this.error = 'A busca não retornou resultados';
        }
      } catch (err) {
        console.error('Erro na busca:', err);
        this.error = 'Erro ao buscar operadoras. Tente novamente mais tarde.';
        if (err.response) {
          if (err.response.status === 404) {
            this.error = 'Nenhum resultado encontrado.';
          } else {
            this.error = `Erro no servidor: ${err.response.status}`;
          }
        }
      } finally {
        this.isLoading = false;
      }
    },

    resetFilters() {
      this.searchQuery = '';
      this.filters = {
        cidade: '',
        uf: '',
        modalidade: ''
      };
      this.results = [];
      this.count = 0;
      this.error = null;
      this.searchPerformed = false;
    },

    formatDate(dateString) {
      if (!dateString) return 'Não informada';
      const date = new Date(dateString);
      return date.toLocaleDateString('pt-BR');
    },

    formatCNPJ(cnpj) {
      if (!cnpj || cnpj.toString().trim() === '') return 'Não informado';
      const cnpjStr = cnpj.toString().padStart(14, '0');
      return cnpjStr.replace(/^(\d{2})(\d{3})(\d{3})(\d{4})(\d{2})$/, '$1.$2.$3/$4-$5');
    },

    formatCEP(cep) {
      if (!cep || cep.toString().trim() === '') return 'Não informado';
      const cepStr = cep.toString().padStart(8, '0');
      return cepStr.replace(/^(\d{5})(\d{3})$/, '$1-$2');
    },

    exportToCSV() {
      if (this.results.length === 0) return;

      let csvContent = "data:text/csv;charset=utf-8,";

      // Cabeçalho
      const headers = [
        'Nome Fantasia', 'Razão Social', 'Registro ANS', 'CNPJ', 'Modalidade',
        'Cidade', 'UF', 'Endereço', 'Telefone', 'E-mail', 'Data Registro ANS'
      ];
      csvContent += headers.join(";") + "\r\n";

      // Dados
      this.results.forEach(item => {
        const endereco = `${item.Logradouro || ''}, ${item.Numero || 'S/N'} ${item.Complemento || ''}`.trim();
        const telefone = item.DDD && item.Telefone ? `(${item.DDD}) ${item.Telefone}` : '';

        const row = [
          `"${item.Nome_Fantasia || ''}"`,
          `"${item.Razao_Social || ''}"`,
          item.Registro_ANS || '',
          this.formatCNPJ(item.CNPJ),
          item.Modalidade || '',
          item.Cidade || '',
          item.UF || '',
          `"${endereco}"`,
          telefone,
          item.Endereco_eletronico || '',
          this.formatDate(item.Data_Registro_ANS)
        ];
        csvContent += row.join(";") + "\r\n";
      });

      // Download
      const encodedUri = encodeURI(csvContent);
      const link = document.createElement("a");
      link.setAttribute("href", encodedUri);
      link.setAttribute("download", `operadoras_${new Date().toISOString().slice(0,10)}.csv`);
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);
    }
  }
};
</script>

<style src="src/assets/css/styles.css"></style>
