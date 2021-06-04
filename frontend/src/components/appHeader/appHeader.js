import React from 'react'
import '../../index.css';
import search from '../../img/search.svg';
import bell from '../../img/bell.svg';
import avatar from '../../img/avatar.png';

const AppHeader = () => {
    return (
        <div className="shapka">
            <div className="menu-small">
                <div className="list-menu">
                    <a className="spisok-menu" href="">Списки</a>
                </div>
                <div className="icon">
                    <a href=""><img className="search" src={search}/></a>
                    <a href=""><img className="bell" src={bell}/></a>
                </div>
            </div>

            <div className="name-avatar">
                <a className="name" href="">Ксюша Донская</a>
                <a href=""><img className="avatar" src={avatar}/></a>
            </div>

        </div>
    )
}

export default AppHeader;
