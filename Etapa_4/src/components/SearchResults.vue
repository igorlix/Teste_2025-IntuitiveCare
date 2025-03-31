<template>
  <div class="search-results">
    <div v-if="isLoading" class="loading-state">
      <div class="spinner"></div>
      <p>Buscando operadoras...</p>
    </div>

    <div v-if="error" class="error-state">
      <IconifyIcon icon="mdi:alert" class="state-icon error-icon" />
      <div class="error-content">
        <h4>Ocorreu um erro</h4>
        <p>{{ error }}</p>
      </div>
      <button @click="$emit('search')" class="retry-button">
        <IconifyIcon icon="mdi:reload" /> Tentar novamente
      </button>
    </div>

    <template v-if="!isLoading && !error">
      <div v-if="results.length > 0" class="results-container">
        <div class="results-header">
          <h3>
            <IconifyIcon icon="mdi:check-circle" class="state-icon success-icon" />
            {{ count }} operadora(s) encontrada(s)
          </h3>
          <div class="results-actions">
            <button @click="$emit('export')" class="action-button export">
              <IconifyIcon icon="mdi:file-export" /> Exportar
            </button>
            <button @click="$emit('reset')" class="action-button reset">
              <IconifyIcon icon="mdi:broom" /> Limpar
            </button>
          </div>
        </div>

        <div class="results-grid">
          <ResultCard
              v-for="(item, index) in results"
              :key="index"
              :item="item"
              @format-cnpj="$emit('format-cnpj', $event)"
              @format-date="$emit('format-date', $event)"
              @format-cep="$emit('format-cep', $event)"
          />
        </div>
      </div>

      <div v-else-if="searchPerformed" class="empty-state">
        <div class="empty-content">
          <IconifyIcon icon="mdi:magnify" class="state-icon empty-icon" />
          <h4>Nenhum resultado encontrado</h4>
          <p>Não encontramos operadoras com os critérios informados.</p>
        </div>
        <button @click="$emit('reset')" class="action-button try-again">
          <IconifyIcon icon="mdi:refresh" /> Limpar filtros e tentar novamente
        </button>
      </div>

      <div v-else class="initial-state">
        <IconifyIcon icon="mdi:magnify-plus-outline" class="state-icon initial-icon" wheight="100" />
        <h4>Realize uma busca</h4>
        <p>Preencha os campos acima para encontrar operadoras de saúde</p>
      </div>
    </template>
  </div>
</template>

<script>
import { Icon as IconifyIcon } from '@iconify/vue';
import ResultCard from './ResultCard.vue';

export default {
  name: 'SearchResults',
  components: {
    ResultCard,
    IconifyIcon
  },
  props: {
    results: Array,
    count: Number,
    isLoading: Boolean,
    error: String,
    searchPerformed: Boolean
  }
};
</script>

<style scoped src="src/assets/css/components/SearchResults.css"></style>