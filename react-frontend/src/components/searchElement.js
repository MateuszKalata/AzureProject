import React from 'react'
import { Container, Card } from 'react-bootstrap'

export default function SearchElement(props) {

    return (
        <Container className="my-3">
            <Card>
                <Card.Body> {props.text}</Card.Body>
            </Card>                  
        </Container>
    )
}