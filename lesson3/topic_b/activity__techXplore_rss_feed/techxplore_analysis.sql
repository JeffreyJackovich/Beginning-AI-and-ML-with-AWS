SELECT tt.topic, 
	tt.term, 
	tt.weight, 
	dt.docname,
    dt.proportion
FROM linkedTopicDB2.tech_xplore_topic_terms tt, linkedTopicDB2.known_structure_doc_topics dt
WHERE tt.topic = dt.topic
ORDER BY topic ASC;