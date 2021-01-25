import React from 'react'
import { Container, Form, Row, Col, Button } from 'react-bootstrap'

import SearchElement from './searchElement'
export default function HomePage(props) {

    const [searchValue, setSearchValue] = React.useState("")
    const [searchElements, setSearchElements] = React.useState([])
    const insertExampleElements = () => {
        const enable_items = [
                {
                    text: "In nec suscipit leo, a congue tellus. Nullam massa magna, hendrerit ut lacus eget, vestibulum elementum est. Aenean venenatis aliquet lectus, suscipit mattis magna. Aenean euismod posuere magna vitae eleifend. Proin interdum vitae enim quis bibendum. Curabitur molestie, magna id cursus aliquam, sapien arcu faucibus arcu, at egestas est tellus ut est. Aliquam erat volutpat. Quisque porta urna sit amet pellentesque lacinia. Morbi dignissim elementum suscipit. In nec tempor massa, elementum cursus lectus. Nulla suscipit, odio a sagittis consequat, quam sem laoreet risus, eu tincidunt nibh mauris sit amet nisl."
                },
                {
                    text: "Proin eu augue facilisis, ultricies neque at, scelerisque nisi. Donec eu urna at lacus eleifend laoreet faucibus quis ligula. Praesent ac maximus enim. Nullam mi felis, tempus vitae interdum id, viverra sed arcu. Aenean ut condimentum augue, id tempus diam. Etiam varius velit ut libero blandit tempor. Proin quis vehicula risus, non malesuada nisl. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Cras efficitur mauris eu tempor laoreet. Pellentesque pretium risus vitae metus vestibulum, ornare suscipit nunc fringilla. Sed vitae rutrum sapien, eu porta est. Aenean id enim mollis, bibendum enim id, bibendum massa."
                },
                {
                    text: "Nunc commodo consectetur leo, at hendrerit est posuere a. Integer congue sed dui at ornare. Aliquam vel placerat metus. Nullam dapibus ultrices turpis id lobortis. Quisque nec porttitor neque. Nam magna lacus, elementum at fermentum sit amet, tempus non nulla. Suspendisse facilisis ligula sed eros elementum eleifend."
                },
                {
                    text: "Fusce eget mauris suscipit odio elementum dictum at eu quam. Nunc pharetra auctor luctus. Phasellus pretium feugiat augue eget egestas. Vestibulum enim odio, dignissim sed vulputate eget, rhoncus at dui. Ut sodales metus quis mi mattis, nec consectetur enim accumsan. Quisque in sapien vulputate, fringilla est ut, convallis libero. Etiam vehicula nisl in magna pharetra fringilla. Ut imperdiet augue nec blandit vehicula. Maecenas in turpis vestibulum, feugiat mi vel, egestas nulla. Proin eu velit eu orci porta tristique. Lorem ipsum dolor sit amet, consectetur adipiscing elit."
                },
                {
                    text: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam neque erat, pharetra id sapien vel, facilisis laoreet nisl. Sed bibendum vehicula sem, id aliquet eros imperdiet id. Morbi ultrices velit quis turpis vulputate vulputate. Orci varius natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Suspendisse potenti. Phasellus dignissim a arcu nec gravida. Morbi nec metus ac justo convallis sollicitudin."
                }
            ]
        const max_found_items = 10
        const min_found_items = 1
        const found_items_length = Math.floor(Math.random() * (max_found_items - min_found_items)) + min_found_items
        const found_items = []
        let i = 0
        for (i=0; i<found_items_length; i++) {
            const item = enable_items[Math.floor(Math.random() * enable_items.length)];
            found_items.push(item)
        }

        setSearchElements(found_items)
    }
    return (
        <Container fluid>
            <Row className="my-3">
                <Col>
                    <h1>Sematic Search</h1>
                </Col>
            </Row>
            <Row className="justify-content-md-center my-3">
                <Col md={6}>
                    <Form.Control
                        type="text"
                        placeholder="Insert statement to search semantic similar paragraphs..."
                        value={searchValue}
                        onChange={(e) => setSearchValue(e.target.value)}
                        />
                </Col>
                <Col md="auto">
                    <Button variant="success" onClick={insertExampleElements}>Search</Button>
                </Col>
            </Row>
            <Row className={"justify-content-md-left" + (searchElements.length === 0? " d-none" : "")}>
                <Col>
                    <h4>Found {searchElements.length} paragraphs:</h4>
                </Col>
            </Row>
            {searchElements.map((elem, idx) =>
                <SearchElement key={idx} text={elem.text} />
            )}
        </Container>
    )
}