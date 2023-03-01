lnd_config_template = \
    "[Application Options]\n" \
    "alias={name}\n" \
    "listen=0.0.0.0:{lnd_port}\n" \
    "restlisten=0.0.0.0:{rest_port}\n" \
    "rpclisten=0.0.0.0:{rpc_port}\n" \
    "debuglevel=info\n" \
    "unsafe-disconnect=1\n" \
    "tlsextradomain=host.docker.internal\n" \
    "tlsautorefresh=true\n" \
    "[Bitcoin]\n" \
    "bitcoin.active=1\n" \
    "bitcoin.regtest=1\n" \
    "bitcoin.node=bitcoind\n" \
    "bitcoin.basefee={base_fee_msat}\n" \
    "bitcoin.feerate={fee_rate}\n" \
    "bitcoin.defaultchanconfs=1\n" \
    "[Bitcoind]\n" \
    "bitcoind.rpchost=0.0.0.0\n" \
    "bitcoind.rpcuser=lnd\n" \
    "bitcoind.rpcpass=123456\n" \
    "bitcoind.zmqpubrawblock=tcp://127.0.0.1:28332\n" \
    "bitcoind.zmqpubrawtx=tcp://127.0.0.1:28333\n" \
    "[routing]\n" \
    "routing.strictgraphpruning=false\n" \
    "[db]\n" \
    "db.no-graph-cache=true\n" \
    "[protocol]\n" \
    "protocol.wumbo-channels=true"

bitcoind_config_template = \
    "txindex=1\n" \
    "zmqpubrawblock=tcp://127.0.0.1:28332\n" \
    "zmqpubrawtx=tcp://127.0.0.1:28333\n" \
    "regtest=1\n" \
    "rpcuser=lnd\n" \
    "rpcpassword=123456\n" \
    "fallbackfee=0.00001000\n" \
    "regtest.rpcbind=0.0.0.0\n" \
    "server=1\n" \
    "rpcallowip=0.0.0.0/0\n"

cln_config_template = \
    "alias={name}\n" \
    "addr=:{port}\n" \
    "bitcoin-rpcconnect=127.0.0.1\n" \
    "bitcoin-rpcport=18443\n" \
    "bitcoin-rpcuser=lnd\n" \
    "bitcoin-rpcpassword=123456\n" \
    "bitcoin-retry-timeout=3600\n" \
    "network=regtest\n" \
    "funding-confirms=1\n" \
    "max-concurrent-htlcs=483\n" \
    "experimental-offers\n" \
    "experimental-dual-fund\n" \
    "wumbo\n"
