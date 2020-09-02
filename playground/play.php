<?php

function removeByIndex(&$array, $unwanted_key) {
    if (!is_array($array) || empty($unwanted_key))
        return false;
    unset($array[$unwanted_key]);
    foreach ($array as &$value) {
        if (is_array($value)) {
            removeByIndex($value, $unwanted_key);
        }
    }
}

$order = [
    'properties' => [
        'refunds' => [
            [
                'transactions' => [
                    [
                        'receipt' => [
                            'charge' => [
                                'balance_transaction' => 1
                            ]
                        ]
                    ]
                ]
            ]
        ]
    ]
];


removeByIndex($order, 'balance_transaction');
var_dump($order);