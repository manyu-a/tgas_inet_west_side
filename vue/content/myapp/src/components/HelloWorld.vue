<template>
<div class="root">
    <v-container>
        <v-card>
            <v-card-title>名前の入力</v-card-title>
            <v-card-text>
                <v-text-field v-model="name" label="名前を入れて「送信する」を押してください">
                </v-text-field>
            </v-card-text>
            <v-divider></v-divider>
            <v-card-actions>
                <v-btn text color="primary" v-on:click="submitForm">
                    送信する
                </v-btn>
            </v-card-actions>
                </v-card>
            <v-card>
            <v-card-title>メッセージ</v-card-title>
                <v-card-text>
                <h4>{{ message }}</h4>
            </v-card-text>
        </v-card>
    </v-container>
    <v-container>
        <v-card>
            <v-card-title>素数かどうかの判定</v-card-title>
            <v-card-text>
                <v-text-field v-model="val" label="数値を入れて「送信する」を押してください">
                </v-text-field>
            </v-card-text>
            <v-divider></v-divider>
            <v-card-actions>
                <v-btn text color="primary" v-on:click="submitval">
                    送信する
                </v-btn>
            </v-card-actions>
                </v-card>
            <v-card>
            <v-card-title>判定結果</v-card-title>
                <v-card-text>
                <h4>{{ prime_bool }}</h4>
            </v-card-text>
        </v-card>
    </v-container>
</div>
</template>
<script type="module">
    import axios from 'axios';
    export default {
        name: 'HelloWorld',

        data: () => ({
            name: 'test',
            message: 'ここにメッセージが表示されます',

            val: '53',
            prime_bool: 'ここに判定結果が表示されます'

        }),

        methods: {
            submitForm: async function () {
                const res = await
                axios.post('http://localhost:8080/api/greetings', {
                    'name': this.name
                    });
                this.message = res.data.message;
            },
            submitval: async function () {
                const res = await
                axios.post('http://localhost:8080/api/eratosthenes', {
                    'val': this.val
                    });
                this.prime_bool = res.data.prime_bool;
            }
        },
    };
</script>