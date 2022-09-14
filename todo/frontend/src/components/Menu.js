import React from "react";

const MenuList = ({menu}) => {
    return (
        <div class='menu'>
            <ul>
                <li><a href="http://127.0.0.1:3000">Пользователи</a></li>
                <li><a href="http://127.0.0.1:8000/admin">Админка</a></li>
                <li><a href="#">ToDO</a></li>
            </ul>
        </div>
    )
}

export default MenuList