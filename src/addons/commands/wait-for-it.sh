#!/usr/bin/env bash
# Use this script to test if a given TCP host/port are available

WAITFORIT_QUIET=0
WAITFORIT_TIMEOUT=15
WAITFORIT_HOST=""
WAITFORIT_PORT=""

echoerr() { if [[ $WAITFORIT_QUIET -ne 1 ]]; then echo "$@" 1>&2; fi }

usage()
{
    echo "Usage: wait-for-it.sh [options] host:port"
    echo "Options:"
    echo "  -h, --host          Hostname or IP address to check"
    echo "  -p, --port          TCP port to check"
    echo "  -t, --timeout       Timeout in seconds (default: 15)"
    echo "  -q, --quiet         Suppress error messages"
    echo "  --help              Show this help message"
}

wait_for()
{
    local start_ts=$(date +%s)

    while :
    do
        (echo > /dev/tcp/$WAITFORIT_HOST/$WAITFORIT_PORT) >/dev/null 2>&1
        result=$?

        if [[ $result -eq 0 ]]; then
            exit 0
        fi

        local now_ts=$(date +%s)
        if [[ $((now_ts - start_ts)) -ge $WAITFORIT_TIMEOUT ]]; then
            echoerr "Timeout occurred after waiting $WAITFORIT_TIMEOUT seconds for $WAITFORIT_HOST:$WAITFORIT_PORT"
            exit 1
        fi

        sleep 1
    done
}

while [[ $# -gt 0 ]]
do
    case "$1" in
        -h|--host)
        WAITFORIT_HOST="$2"
        shift 2
        ;;
        -p|--port)
        WAITFORIT_PORT="$2"
        shift 2
        ;;
        -t|--timeout)
        WAITFORIT_TIMEOUT="$2"
        shift 2
        ;;
        -q|--quiet)
        WAITFORIT_QUIET=1
        shift 1
        ;;
        --help)
        usage
        exit 0
        ;;
        *)
        if [[ "$1" =~ ^[a-zA-Z0-9._-]+:[0-9]+$ ]]; then
            WAITFORIT_HOST=$(echo "$1" | cut -d: -f1)
            WAITFORIT_PORT=$(echo "$1" | cut -d: -f2)
            shift 1
        else
            echoerr "Unknown argument: $1"
            usage
            exit 1
        fi
        ;;
    esac
done

if [[ -z "$WAITFORIT_HOST" || -z "$WAITFORIT_PORT" ]]; then
    echoerr "Error: You need to provide a host and port"
    usage
    exit 1
fi

wait_for
