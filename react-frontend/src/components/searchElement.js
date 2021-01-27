import React from 'react'
import { Container, Card, Row, Col } from 'react-bootstrap'

export default function SearchElement(props) {
    return (
        <Container className="my-3">
            <Card>
                <Card.Body>
                    <Row>
                        <Col md={2}>
                            <h6 className="text-left">Title:</h6>
                        </Col>
                        <Col md={9}>
                            <p className="text-left">{props.item.title}</p>
                        </Col>
                    </Row>
                    <Row>
                        <Col md={2}>
                            <h6 className="text-left">Paragraph:</h6>
                        </Col>
                        <Col md={9}>
                            <p className="text-left">{props.item.paragraph}</p>
                        </Col>
                    </Row>
                    <Row>
                        <Col md={2}>
                            <h6 className="text-left">Url:</h6>
                        </Col>
                        <Col md="auto">
                            <a className="text-left" href={props.item.url}>{props.item.url}</a>
                        </Col>
                    </Row>
                    <Row>
                        <Col md={2}>
                            <h6 className="text-left">Index:</h6>
                        </Col>
                        <Col md="auto">
                            <p className="text-left">{props.item.index}</p>
                        </Col>
                    </Row>
                </Card.Body>
            </Card>                  
        </Container>
    )
}