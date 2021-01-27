import React from 'react'
import { Container, Form, Row, Col, Button, Spinner } from 'react-bootstrap'
import * as actionCreators from "../store/actions";
import { withRouter } from 'react-router-dom'
import {connect} from 'react-redux';

import SearchElement from './searchElement'
function HomePage(props) {

    const [searchValue, setSearchValue] = React.useState("")
    const [searchElements, setSearchElements] = React.useState([])

    React.useEffect(() => {
        setSearchElements(JSON.parse(JSON.stringify(props.elements)))
    }, [props.elements])

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
                    <Button
                        variant="success"
                        onClick={ () => {
                            props.fetchElements(searchValue)
                        }}
                        >
                        Search
                    </Button>
                </Col>
                <Col md={1} className={props.isLoading? "" : "d-none"} >
                    <Spinner animation="border" role="status">
                        <span className="sr-only">Loading...</span>
                    </Spinner>
                </Col>
            </Row>
            <Row className={"justify-content-md-left" + (searchElements.length === 0? " d-none" : "")}>
                <Col>
                    <h4>Found {searchElements.length} paragraphs:</h4>
                </Col>
            </Row>
            {searchElements.map((elem, idx) =>
                <SearchElement key={idx} text={elem.paragraph} item={elem} />
            )}
        </Container>
    )
}
const mapStateToProps = (state) => {
	return {
        elements: state.searches.elements,
        isLoading: state.searches.isLoading,
	};
};

const mapDispatchToProps = (dispatch) => ({
	fetchElements: (query) =>
		dispatch(actionCreators.fetchElements(query)),
});

export default withRouter(connect(mapStateToProps, mapDispatchToProps)(HomePage));