WAIT_TIME = range(1, 2) # Ожидание перед след дейсвием бота
RATIO_STARGATE_SINGLE = 0.5  # Кэф. для single сетей, сколько отправлять STARGATE в другую сеть

# Все аквтиности
NO_ACTIVITY       = 'NO ACTIVITY'
STARGATE          = 'STARGATE'
STARGATE_LIQ      = 'STARGATE_LIQ'
STARGATE_STG      = 'STARGATE_STG'
BTC_BRIDGE        = 'BTC_BRIDGE'
TESTNET_BRIDGE    = 'TESTNET_BRIDGE'
APTOS_BRIDGE      = 'APTOS_BRIDGE'
SWAP_TOKEN        = 'SWAP_TOKEN'
STARGATE_BSC      = 'STARGATE_BSC'
STARGATE_ARBITRUM = 'STARGATE_ARBITRUM'
STARGATE_OPTIMISM = 'STARGATE_OPTIMISM'
HARMONY_BRIDGE    = 'HARMONY_BRIDGE'

# Активности, которые всегда надо проверять
ACTIVITY_LIST = [
    STARGATE_LIQ,
    STARGATE_STG,
    BTC_BRIDGE,
    TESTNET_BRIDGE,
    SWAP_TOKEN,
    APTOS_BRIDGE,
    HARMONY_BRIDGE,
]

# Сети, в которые можно отправлять из основного блока STARGATE
STARGATE_CHAIN_LIST = [
    'Avalanche',
    'Polygon',
]
