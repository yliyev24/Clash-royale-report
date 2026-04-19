// Clash Royale binary packet strukturu (C++)

struct GamePacket {
    uint16_t message_id;    // Mesaj növü
    uint32_t timestamp;     // Millisaniyə timestamp
    uint32_t player_id;     // Oyunçu ID
    uint8_t  payload[];     // Şifrəli məlumat
};

// EndClientTurn (ECT) paketi göndərmə
void sendEndClientTurn(GameSession& session) {
    GamePacket pkt;
    pkt.message_id = MSG_END_CLIENT_TURN;  // 0x0581
    pkt.timestamp  = getCurrentTick();
    pkt.player_id  = session.playerId;
    encryptAndSend(session.socket, pkt);
}
