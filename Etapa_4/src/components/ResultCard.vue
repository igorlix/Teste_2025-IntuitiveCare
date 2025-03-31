<template>
  <div class="result-card">
    <div class="card-header">
      <div class="card-badge" :class="getModalidadeClass(item.Modalidade)">
        {{ getModalidadeShort(item.Modalidade) }}
      </div>
      <div class="card-title">
        <h4>{{ item.Nome_Fantasia || 'Nome não disponível' }}</h4>
        <div class="card-meta">
          <span class="ans-number">{{ item.Registro_ANS || 'N/I' }}</span>
          <span class="card-date" v-if="item.Data_Registro_ANS">
            <i class="far fa-calendar-alt"></i> {{ ('format-date', item.Data_Registro_ANS) }}
          </span>
        </div>
      </div>
    </div>

    <div class="card-body">
      <div class="info-section">
        <div class="info-item">
          <i class="fas fa-building"></i>
          <div>
            <label>Razão Social</label>
            <p>{{ item.Razao_Social || 'Não informada' }}</p>
          </div>
        </div>

        <div class="info-item">
          <i class="fas fa-id-card"></i>
          <div>
            <label>CNPJ</label>
            <p>{{('format-cnpj', item.CNPJ) }}</p>
          </div>
        </div>
      </div>

      <div class="info-section">
        <div class="info-item">
          <i class="fas fa-map-marker-alt"></i>
          <div>
            <label>Endereço</label>
            <p>
              {{ item.Logradouro || 'Endereço não informado' }},
              {{ item.Numero || 'S/N' }}
              <span v-if="item.Complemento"> - {{ item.Complemento }}</span>
            </p>
            <p>{{ item.Bairro || 'Bairro não informado' }}</p>
            <p>{{ item.Cidade || 'Cidade não informada' }}/{{ item.UF || 'UF não informada' }}</p>
            <p><strong>CEP:</strong> {{('format-cep', item.CEP) }}</p>
          </div>
        </div>
      </div>

      <div class="info-section">
        <div class="info-item">
          <i class="fas fa-phone"></i>
          <div>
            <label>Contatos</label>
            <p v-if="item.DDD && item.Telefone">
              <strong>Telefone:</strong> ({{ item.DDD }}) {{ item.Telefone }}
            </p>
            <p v-if="item.Fax">
              <strong>Fax:</strong> {{ item.Fax }}
            </p>
            <p v-if="item.Endereco_eletronico">
              <strong>E-mail:</strong> {{ item.Endereco_eletronico }}
            </p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ResultCard',
  props: {
    item: Object
  },
  methods: {
    getModalidadeClass(modalidade) {
      if (!modalidade) return 'default';

      const classes = {
        'Seguradora Especializada em Saúde': 'seguradora',
        'Cooperativa Médica': 'cooperativa-medica',
        'Cooperativa Odontológica': 'cooperativa-odonto',
        'Odontologia de Grupo': 'odonto-grupo',
        'Medicina de Grupo': 'medicina-grupo',
        'Autogestão': 'autogestao',
        'Filantropia': 'filantropia'
      };

      return classes[modalidade] || 'default';
    },

    getModalidadeShort(modalidade) {
      if (!modalidade) return 'N/I';

      const shorts = {
        'Seguradora Especializada em Saúde': 'Seguradora',
        'Cooperativa Médica': 'Coop. Médica',
        'Cooperativa Odontológica': 'Coop. Odonto',
        'Odontologia de Grupo': 'Odonto Grupo',
        'Medicina de Grupo': 'Medicina Grupo',
        'Autogestão': 'Autogestão',
        'Filantropia': 'Filantropia'
      };

      return shorts[modalidade] || modalidade;
    }
  }
}
</script>

<style scoped src="src/assets/css/components/ResultCard.css"></style>