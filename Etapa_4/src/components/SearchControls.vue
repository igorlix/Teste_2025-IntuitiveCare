<template>
  <div class="search-controls">
    <div class="main-search">
      <div class="search-input-container">
        <IconifyIcon icon="mdi:magnify" class="search-icon" />
        <input
            type="text"
            :value="searchQuery"
            @input="$emit('update:searchQuery', $event.target.value)"
            @keyup.enter="$emit('search')"
            placeholder="Digite nome, razão social ou registro ANS..."
            class="search-input"
        />
      </div>
      <button @click="$emit('search')" class="search-button">
        <span>Buscar</span>
        <IconifyIcon icon="mdi:arrow-right" />
      </button>
    </div>

    <div class="filters-accordion">
      <div class="accordion-header" @click="toggleFilters">
        <span>Filtros Avançados</span>
        <IconifyIcon :icon="showFilters ? 'mdi:chevron-up' : 'mdi:chevron-down'" />
      </div>

      <transition name="fade">
        <div v-if="showFilters" class="filters-container">
          <div class="filter-section">
            <h4>
              <IconifyIcon icon="mdi:map-marker" />
              Localização
            </h4>
            <div class="filter-group">
              <label for="uf">Estado (UF)</label>
              <div class="select-wrapper">
                <select
                    id="uf"
                    :value="filters.uf"
                    @change="$emit('update:filters', { ...filters, uf: $event.target.value })"
                >
                  <option value="">Todos os estados</option>
                  <option v-for="state in estados" :value="state" :key="state">{{ state }}</option>
                </select>
                <IconifyIcon icon="mdi:chevron-down" />
              </div>
            </div>

            <!-- Ícone corrigido para cidade -->
            <div class="filter-group">

              <label for="cidade">
                <IconifyIcon icon="mdi:city" class="input-icon" />
                Cidade</label>
              <div class="input-with-icon">
                <input
                    id="cidade"
                    type="text"
                    :value="filters.cidade"
                    @input="$emit('update:filters', { ...filters, cidade: $event.target.value })"
                    placeholder="Filtrar por cidade"
                />
              </div>
            </div>
          </div>

          <div class="filter-section">
            <h4>
              <IconifyIcon icon="mdi:tag" />
              Modalidade
            </h4>
            <div class="filter-group">
              <label for="modalidade">Tipo de Operadora</label>
              <div class="select-wrapper">
                <select
                    id="modalidade"
                    :value="filters.modalidade"
                    @change="$emit('update:filters', { ...filters, modalidade: $event.target.value })"
                >
                  <option value="">Todas modalidades</option>
                  <option v-for="mod in modalidades" :value="mod" :key="mod">{{ mod }}</option>
                </select>
                <IconifyIcon icon="mdi:chevron-down" />
              </div>
            </div>
          </div>
        </div>
      </transition>
    </div>
  </div>
</template>

<script>
import { Icon as IconifyIcon } from '@iconify/vue';

export default {
  name: 'SearchControls',
  components: {
    IconifyIcon
  },
  props: {
    searchQuery: String,
    filters: Object,
    estados: Array,
    modalidades: Array
  },
  data() {
    return {
      showFilters: false
    };
  },
  methods: {
    toggleFilters() {
      this.showFilters = !this.showFilters;
    }
  }
};
</script>

<style scoped src="src/assets/css/components/SearchControls.css"></style>