% Clash Royale tərzi Erlang oyun serveri

-module(battle_server).
-behaviour(gen_server).

% Yeni döyüş prosesi başlatmaq
start_battle(Player1, Player2) ->
    gen_server:start_link(?MODULE,
        [Player1, Player2], []).

% Kart yerləşdirmə hadisəsini emal etmək
handle_cast({place_card, PlayerId, CardId, X, Y}, State) ->
    NewState = game_logic:place_card(
        State, PlayerId, CardId, X, Y),
    broadcast_state(NewState),
    {noreply, NewState};

% Döyüş bitdikdə nəticəni göndər
handle_info(battle_end, State) ->
    notify_players(State#battle.winner),
    {stop, normal, State}.
