<template>
  <div class="search-header">
    <h1>Busca de Operadoras de Saúde</h1>
    <p class="subtitle">Consulte a base de dados da Agência Nacional de Saúde Suplementar</p>
    <div class="header-decoration">
      <div class="decoration-line"></div>
      <IconifyIcon icon="mdi:heart-pulse" class="heart-icon" height="80" />
      <div class="decoration-line"></div>
    </div>
  </div>
</template>

<script>
import { Icon as IconifyIcon } from '@iconify/vue';

export default {
  name: 'SearchHeader',
  components: {
    IconifyIcon
  }
}
</script>

<style scoped src="src/assets/css/components/SearchHeader.css"></style>