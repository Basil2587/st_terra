import  React, { useEffect, useState } from  'react';
import {getResults} from '../../../ResultService';
import AddItem from './listComponents/addItem'
import ListItem from './listItem';
import bookImg from '../../../img/bookImg.png';
import laptopImg from '../../../img/laptopImg.png';

const ListPage = (props) => {

    const [results, setResults] = useState([])   

    useEffect(() => {
        getResults('lists/')
        .then(function (result) {
            setResults(result);
        });
    }, [])

    const [toggle, setToggle] = useState(false);

    const modal = toggle ? <AddItem toggle={toggle} setToggle={setToggle} hideModal={() => hideModal()}/> : null;

    const toggleList = () => setToggle(!toggle);

    const hideModal = () => setToggle(!toggle);

    const list = document.querySelector('.list')

    document.addEventListener('keydown', (e) => {
        if (e.code === "Escape" && toggle === true) { 
            setToggle(!toggle);
        }
    });

            //     {/* {
            //     results.map((item) => <label>{item.data}</label>)
            // } */}
    return (      


        <div className="list float-start" onClick={e => e.target === list && toggle === true ? setToggle(!toggle) : null}>
            <div className="d-flex justify-content-around">
                <ListItem toggleList={toggleList} data={results.books} img={false}/>
                <ListItem toggleList={toggleList} data={results.films} img={bookImg}/>
                <ListItem toggleList={toggleList} data={results.travels} img={false}/>
                <ListItem toggleList={toggleList} data={results.wishes} img={laptopImg}/>
            </div>
            {modal}

        </div>
    );
}

export  default  ListPage;


    // handleDelete(e,pk){
    //     var  self  =  this;
    //     customersService.deleteCustomer({pk :  pk}).then(()=>{
    //         var  newArr  =  self.state.customers.filter(function(obj) {
    //             return  obj.pk  !==  pk;
    //         });

    //         self.setState({customers:  newArr})
    //     });
    // }
