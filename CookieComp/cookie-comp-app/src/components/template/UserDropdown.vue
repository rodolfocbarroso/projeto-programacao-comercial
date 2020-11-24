<template>
  <v-menu bottom min-width="200px" rounded offset-y>
    <template v-slot:activator="{ on }">
      <v-btn text height="56px" v-on="on">
        <v-avatar size="36px">
          <Gravatar :email="user.email" alt="User" />
        </v-avatar>
        <v-icon>mdi-menu-down</v-icon>
      </v-btn>
    </template>

    <v-card width="230px">
      <v-list>
        <v-list-item>
          <v-list-item-avatar>
            <v-avatar size="36px">
              <Gravatar :email="user.email" alt="User" />
            </v-avatar>
          </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title>
              {{ user.name }}
            </v-list-item-title>
            <v-list-item-subtitle>
              {{ user.email }}
            </v-list-item-subtitle>
          </v-list-item-content>
        </v-list-item>
      </v-list>

      <v-divider></v-divider>

      <v-list>
        <v-list-item>
          <v-btn width="200px" large depressed text>
            <v-icon>mdi-cogs</v-icon>
            Administração
          </v-btn>
        </v-list-item>
        <v-list-item>
          <v-btn width="200px" large depressed text>
            <v-icon>mdi-exit-to-app</v-icon>
            Sair
          </v-btn>
        </v-list-item>
      </v-list>
    </v-card>
  </v-menu>
</template>

<script>
import { mapState } from "vuex";
import Gravatar from "vue-gravatar";

export default {
  name: "UserDropdown",
  components: { Gravatar },
  computed: mapState(["user"]),
};
</script>

<style>
</style>