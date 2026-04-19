// Supercell ID autentifikasiyası (JavaScript)

async function loginWithSupercellId(token) {
    const response = await fetch(
        'https://id.supercell.com/api/authenticate',
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                gameId: 'clash_royale',
                token: token,
            })
        }
    );

    const data = await response.json();
    // Signed token → game server-ə göndər
    return data.signedToken;
}
