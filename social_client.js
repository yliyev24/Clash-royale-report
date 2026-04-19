// Supercell sosial layer WebSocket (JavaScript)

class SupercellSocialClient {
    constructor(playerId) {
        this.ws = new WebSocket(
            'wss://social.supercell.com/connect'
        );
        this.playerId = playerId;
    }

    subscribe(topic) {
        this.ws.send(JSON.stringify({
            type: 'SUBSCRIBE',
            topic: topic,   // 'friends', 'clan', 'chat'
            playerId: this.playerId
        }));
    }

    onMessage(handler) {
        this.ws.onmessage = (event) => {
            const msg = JSON.parse(event.data);
            handler(msg);
        };
    }
}
