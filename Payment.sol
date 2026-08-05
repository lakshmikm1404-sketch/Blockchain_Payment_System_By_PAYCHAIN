// SPDX-License-Identifier: MIT

pragma solidity ^0.8.20;

contract Payment {

    address public merchant;

    constructor() {
        merchant = msg.sender;
    }

    event Paid(
        address sender,
        uint256 amount
    );

    function pay()
        external
        payable
    {
        emit Paid(
            msg.sender,
            msg.value
        );
    }

    function withdraw()
        external
    {
        require(
            msg.sender == merchant,
            "Only merchant"
        );

        payable(merchant).transfer(
            address(this).balance
        );
    }
}